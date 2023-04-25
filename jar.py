Class Jar:
    Def __init__(self, capacity=12):
        If not isinstance(capacity, int) or capacity < 0:
            Raise ValueError(“Capacity must be a non-negative integer”)
        Self._capacity = capacity
        Self._size = 0

    Def __str__(self):
        Return “🍪” * self._size

    Def deposit(self, n):
        If not isinstance(n, int) or n < 0:
            Raise ValueError(“Deposit amount must be a non-negative integer”)
        If self._size + n > self._capacity:
            Raise ValueError(“Cookie jar is full”)
        Self._size += n

    Def withdraw(self, n):
        If not isinstance(n, int) or n < 0:
            Raise ValueError(“Withdrawal amount must be a non-negative integer”)
        If self._size – n < 0:
            Raise ValueError(“Cookie jar is empty”)
        Self._size -= n

    @property
    Def capacity(self):
        Return self._capacity

    @property
    Def size(self):
        Return self._size
