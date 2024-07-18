# Task 1

def caching_fibonacci():
    # Функція повертає внутрішню функцію fibonacci
    cache = {}
    def fibonacci(n):
        # Обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція повертає значення з кешу
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci
    # КІНЕЦЬ ФУНКЦІЇ caching_fibonacci



# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(20))  # Виведе 6765
