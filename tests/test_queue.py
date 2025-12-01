import pytest  # type: ignore[import-not-found]
from src.ds.queue import Queue
from src.core.errors import EmptyError

def test_enqueue_and_front():
    queue = Queue()
    assert queue.is_empty()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert not queue.is_empty()
    assert queue.front() == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.front() == 2
    assert queue.dequeue() == 2
    assert queue.front() == 3
    assert queue.dequeue() == 3
    assert queue.is_empty()


def test_empty_queue():
    queue = Queue()
    with pytest.raises(EmptyError):
        queue.dequeue()
    with pytest.raises(EmptyError):
        queue.front()

def test_len():
    queue = Queue()
    assert len(queue) == 0
    queue.enqueue(1)
    assert len(queue) == 1
    queue.enqueue(2)
    assert len(queue) == 2
    queue.dequeue()
    assert len(queue) == 1
    queue.dequeue()
    assert len(queue) == 0
