from typing import TypeVar, Generic, Callable, Self, Any, List

T = TypeVar('T')


class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls.__name__ not in cls._instances:
			cls._instances[cls.__name__] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls.__name__]


class Signal(Generic[T]):
	def __init__(self):
		self.__listeners: List[Callable[[T], Any]] = []

	def emit(self, data: T) -> None:
		for func in self.__listeners:
			func(data)

	def add_listener(self, listener: Callable[[T], Any]) -> None:
		self.__listeners.append(listener)

	def remove_listener(self, listener: Callable[[T], Any]) -> None:
		if listener in self.__listeners:
			self.__listeners.remove(listener)

	def __iadd__(self, listener: Callable[[T], Any]) -> Self:
		self.add_listener(listener)
		return self

	def __isub__(self, listener: Callable[[T], Any]) -> Self:
		self.remove_listener(listener)
		return self
