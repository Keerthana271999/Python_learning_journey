def count_digits(number):
    digits=0
    for num in str(number):
        digits+=1
    print(f"Total no of digits in {number} - {digits}")
count_digits(123456789987654321)