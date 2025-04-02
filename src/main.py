from graphics import *

def get_valid_input(prompt):
    valid_credits = [0, 20, 40, 60, 80, 100, 120]
    while True:
        try:
            value = int(input(prompt))
            if value in valid_credits:
                return value
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")

def classify_student(pass1, defer, fail):
    if pass1 == 120:
        return "Progress"
    elif pass1 == 100:
        return "Progress (Module Trailer)"
    elif fail >= 80:
        return "Exclude"
    else:
        return "Do Not Progress (Module Retriever)"

def display_histogram(progress, trailer, retriever, exclude):
    win = GraphWin("Histogram", 500, 600)
    
    title = Text(Point(250, 40), "Histogram Results")
    title.setStyle("bold")
    title.setSize(15)
    title.draw(win)
    
    line = Line(Point(50, 500), Point(450, 500))
    line.draw(win)
    
    categories = [("Progress", progress, 100),
                  ("Trailer", trailer, 200),
                  ("Retriever", retriever, 300),
                  ("Excluded", exclude, 400)]
    
    colors = ["green", "yellow", "orange", "red"]
    
    for i, (label, count, x_pos) in enumerate(categories):
        rect = Rectangle(Point(x_pos - 40, 500), Point(x_pos + 40, 500 - count * 50))
        rect.setFill(colors[i])
        rect.draw(win)
        
        text = Text(Point(x_pos, 520), label)
        text.setStyle("bold")
        text.draw(win)
        
        count_text = Text(Point(x_pos, 500 - count * 50 - 10), str(count))
        count_text.draw(win)
    
    # Handle window closing error
    try:
        win.getMouse()
    except GraphicsError:
        pass
    
    win.close()

def main():
    progress = trailer = retriever = exclude = 0
    
    while True:
        pass1 = get_valid_input("Please enter your credits at PASS: ")
        defer = get_valid_input("Please enter your credits at DEFER: ")
        fail = get_valid_input("Please enter your credits at FAIL: ")
        
        if pass1 + defer + fail != 120:
            print("Total incorrect. Please re-enter the values.")
            continue
        
        result = classify_student(pass1, defer, fail)
        print(result)
        
        if result == "Progress":
            progress += 1
        elif result == "Progress (Module Trailer)":
            trailer += 1
        elif result == "Exclude":
            exclude += 1
        else:
            retriever += 1
        
        while True:
            user_input = input("Enter 'y' to continue or 'q' to quit and view results: ").lower()
            if user_input == 'q':
                display_histogram(progress, trailer, retriever, exclude)
                
                print("\nFinal Results:") 
                print(f"Progress: {progress}, Trailer: {trailer}, Retriever: {retriever}, Excluded: {exclude}")
                
                # Write the results to note.txt
                try:
                    with open("note.txt", "a") as file:
                        file.write("\nFinal Results:\n")
                        file.write(f"Progress: {progress}, Trailer: {trailer}, Retriever: {retriever}, Excluded: {exclude}\n")
                        print("\nResults written to note.txt.")
                except Exception as e:
                    print(f"Error writing to file: {e}")
                
                # Attempt to read and print the contents of note.txt
                try:
                    with open("note.txt", "r") as file:
                        print("\nContents of note.txt:")
                        print(file.read())
                except FileNotFoundError:
                    print("note.txt not found.")
                
                return
            elif user_input == 'y':
                break
            else:
                print("Invalid input, please enter 'y' or 'q'.")


if __name__ == "__main__":
    main()
