from urllib import request, error #Importing request is to request url  and error is to handle the error if user is offline

#1. perfect sum calculator
def perfect_num_sum_calculator(n,m):
    """Takes parameters 'n' for starting range and 
    'm' for ending range"""
    def is_perfect(num):
        """This is another function to check if each number
        in the range of perfect_sum_calculator fuction is a perfect number"""
        if num<2:
            return False
        divisors_sum=0
        for i in range(1,num):
            if num%i==0:
                divisors_sum+=i
        return divisors_sum==num
    total=0
    
    for i in range(n,m+1):
        if is_perfect(i):
            total+=i
    return total

#2. weight unit converter
def weight_unit_conv(w,conv_unit):
    conv_unit.upper()
    while True:
        if conv_unit=="k":
            print(f"{w}kilograms = {(w*2.20462):.2f}pounds")
            break
        elif conv_unit=="p":
            print(f"{w}kilograms = {(w*0.453592):.2f}pounds")
            break
        else:
            raise ValueError("Type only 'k' for kg to lbs or 'p' forlbs to kg")

#3. Vowel Counter
def vowel_counter(s):
    vowels=['a','e','i','o','u']
    count={letter: s.lower().count(letter.lower()) for letter in vowels}
    vowel_counts=sum(count.values())
    return vowel_counts

#4. Average and Range Finder
def avg_range(lth,lst):
    avg=sum(lst)/lth
    ran=max(lst)-min(lst)
    print(f"Average: {avg} \nRange: {ran}")

#5. String Reverser and Word count
def str_rev_and_wrd_count(text):
    strip_text=text.strip()
    words=strip_text.split()
    word_count=len(words)
    rev_text=strip_text[::-1]
    print(f"{text} : {rev_text}.\nWord Count: {word_count}")

#6. Specific Word Counter
def specific_wrd_counter(url):
    respond=request.urlopen(url)
    read_text=respond.read().decode('utf-8').lower()
    words=read_text.split()
    word_list=["is", "are", "has", "have"]
    print(f"For the url: {url}")
    for word in word_list:
        count = words.count(word)
        print(f"\'{word}\': {count}, ")

def specific_wrd_counter_offline(file):
    with open(file,'r',encoding='utf-8') as f:
        read_text=f.read().lower()
    words=read_text.split()
    word_list=["is", "are", "has", "have"]
    print(f"For the file: {file}")
    for word in word_list:
        count = words.count(word)
        print(f"\'{word}\': {count}, ")

# Exit or continue
def exit_continue():
    while True:
        choice=input("\nWould you like to try another function? (y/n): ").lower()
        if choice=='y':
            return True
        elif choice=='n':
            print("Exiting Program...")
            return False
        else:
            print("Please enter only 'y' for yes and 'n' for no ")



###########---------MAIN--------###############

print("HELLO USER!")
running=True
while running:
    while True:
        print("\nMENU.")
        print("1. Perfect Number Sum Calculator\n2. Weight Unit Converter\n3. Vowel Counter\n4. Average and Range Finder\n5. String Reverser with Word Count\n6. Specific Word Counter\n0. Exit Program\n")
        fx_choice=input("Enter your choice: ")

        if fx_choice=='1':
            while True:
                try:
                    start_range=int(input("Enter a start range: "))
                    while True:
                        try:
                            end_range=int(input("Enter an end range: "))
                            print(f"Perfect Number Sum: {perfect_num_sum_calculator(start_range,end_range)}") 
                            break 
                        except ValueError:
                            print("Invalid num\n")
                    break
                except ValueError:
                    print("Invalid num\n")
            if not exit_continue():
                running = False
                break

        elif fx_choice=='2':
            while True:
                try:
                    weight=float(input("Enter the weight you want to convert: "))
                    while True:
                        try:
                            ktp_or_ptk=input("Would you like to convert from kg to lbs (k) or lbs to kg (p): ").lower()
                            weight_unit_conv(weight,ktp_or_ptk)
                            break
                        except:
                            print("Enter kg to lbs (k) or lbs to kg (p)\n")
                    break
                except ValueError:
                    print(f"Enter valid weight\n")
            if not exit_continue():
                running = False
                break

        elif fx_choice=='3':
            text_str=input("Enter a text: ")
            print(f"\"{text_str}\" contains {vowel_counter(text_str)} vowels")
            if not exit_continue():
                running = False
                break

        elif fx_choice=='4':
            while True:
                try:
                    length=int(input("How many numbers would you like to enter: "))
                    list_of_num=[]
                    for i in range(1,length+1):
                        while True:
                            try:
                                x=int(input(f"{i}.Enter a number: "))
                                break
                            except ValueError as e:
                                print(f"Error: {e}\n")

                        list_of_num.append(x)
                    break
                except ValueError as e:
                    print(f"Error: {e}\n")

            avg_range(length,list_of_num)
            if not exit_continue():
                running = False
                break
        
        elif fx_choice=='5':
            str_text=input("Enter a text: ")
            str_rev_and_wrd_count(str_text)
            if not exit_continue():
                running = False
                break
            
        elif fx_choice=='6':
            url='https://gist.githubusercontent.com/konrados/a1289ade329ac6f4598ebf5ee3dbcb3c/raw/47a5c6473466fff45acf877eb81d6e496d7b001b/story.txt'
            file='local.txt'
            try:
                specific_wrd_counter(url)
            except error.URLError or error.URLError:
                specific_wrd_counter_offline(file)
            if not exit_continue():
                running = False
                break

        elif fx_choice=='0':
            print("Exiting Program...")
            running=False
            break

        else:
            print("Enter a valid choice (1-6)")












    