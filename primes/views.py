from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request, 'input.html')

def prime_number(request):
    if request.method == 'POST':
        number = int(request.POST.get('number', 0))
        primes = primes_generator(number)
        return render(request, 'output.html', {'primes': primes, 'number': number})
    else:
        return render(request, 'input.html')


def primes_generator(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True