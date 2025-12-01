from src.core.errors import EmptyError
from src.core.logging import log_and_raise

class Queue:
    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._in_stack:list = []
        self._out_stack:list = []

    def enqueue(self, x: int) -> None:
        """Add value x to the back of the queue."""
        self._in_stack.append(x)

    def _move_in_to_out(self) -> None:
        """
        Moves all elements from _in_stack to _out_stack
        """
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

    def dequeue(self) -> int:
        """
        Remove and return the front element.
        Raise EmptyError if the queue is empty.
        """
        self._move_in_to_out()

        if not self._out_stack:
            log_and_raise(EmptyError("Queue is empty"))

        return self._out_stack.pop()

    def front(self) -> int:
        """
        Return the front element without removing it.
        Raise EmptyError if the queue is empty.
        """
        self._move_in_to_out()

        if not self._out_stack:
            log_and_raise(EmptyError("Queue is empty"))

        return self._out_stack[-1]

    def is_empty(self) -> bool:
        """Return True if the queue has no elements."""
        return not (self._in_stack or self._out_stack)

    def __len__(self) -> int:
        """Return number of elements in the queue."""
        return len(self._in_stack) + len(self._out_stack)
