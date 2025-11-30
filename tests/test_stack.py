import pytest
from src.ds.stack import Stack
from src.core.errors import EmptyError

def test_push_and_peek():
    stack = Stack()
    assert stack.is_empty()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert not stack.is_empty() 
    assert stack.peek() == 3

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.is_empty()

def test_min():
    stack = Stack()
    stack.push(3)
    assert stack.min() == 3
    stack.push(2)
    assert stack.min() == 2
    stack.push(1)
    assert stack.min() == 1

    stack.pop()
    assert stack.min() == 2
    stack.pop()
    assert stack.min() == 3
    stack.pop()
    assert stack.is_empty()

def test_empty_stack():
    stack = Stack()
    with pytest.raises(EmptyError):
        stack.pop()
    with pytest.raises(EmptyError):
        stack.peek()
    with pytest.raises(EmptyError):
        stack.min()

def test_len():
    stack = Stack()
    assert len(stack) == 0
    stack.push(1)
    assert len(stack) == 1
    stack.push(2)
    assert len(stack) == 2
    stack.pop()
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0

