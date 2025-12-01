from src.core.errors import EmptyError
from src.core.logging import log_and_raise

class Stack:
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._data = []
        self._mins = []

    def push(self, x: int) -> None:
        """Push value x on top of the stack."""
        self._data.append(x)

        if not self._mins:
            self._mins.append(x)
        elif x <= self._mins[-1]:
            self._mins.append(x)
            
    def pop(self) -> int:
        """
        Remove and return the top element.
        Raise EmptyError if the stack is empty.
        """
        if not self._data:
            log_and_raise(EmptyError("Stack is empty"))

        popped = self._data.pop()

        if popped == self._mins[-1]:
            self._mins.pop()
        
        return popped

    def peek(self) -> int:
        """
        Return the top element without removing it.
        Raise EmptyError if the stack is empty.
        """
        if not self._data:
            log_and_raise(EmptyError("Stack is empty"))

        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no elements."""
        return not self._data

    def __len__(self) -> int:
        """Return number of elements in the stack."""
        return len(self._data)

    def min(self) -> int:
        """
        Return the minimum element in the stack.
        For Medium: must be O(1).
        Raise EmptyError if the stack is empty.
        """
        if not self._mins:
            log_and_raise(EmptyError("Stack is empty"))            

        return self._mins[-1]
