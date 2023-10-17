def progress_bar(length, percent):
    fill = int(length * percent / 100)
    bar = '|' + '=' * fill + '-' * (length - fill) + '|'
    print(bar)
    print(str(percent) + '%')

length_of_progress_bar = int(input("Enter the length of the progress bar: "))
percent_of_progress_bar = int(input("Enter the percentage of the progress bar: "))

if (percent_of_progress_bar < 0 or percent_of_progress_bar > 100) or length_of_progress_bar < 0:
    print("Error: Percentage should be between 0 and 100, and the length of the progress bar should be > 0")
else:
    progress_bar(length_of_progress_bar, percent_of_progress_bar)
