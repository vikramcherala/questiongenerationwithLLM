import os

# Updated Directory where the individual question files will be saved
base_output_dir = "/home/vikram/Downloads/DI-demo/timedistance/"

codes = [
    "TDAAA", "TDABB", "TDACC", "TDADD", "TDAEE", "TDAFF", "TDAGG", "TDAHH", 
    "TDAII", "TDAJJ", "TDALL", "TDAMM", "TDANN", "TDAOO", "TDAPP", "TDAQQ", 
    "TDARR", "TDASS", "TDATT", "TDAUU", "TDAVV", "TDAWW", "TDAXX", "TDAYY", 
    "TDAZZ", "TDBAA", "TDBBB", "TDBCC", "TDBDD", "TDBEE", "TDBFF", "TDBGG", 
    "TDBHH", "TDBII", "TDBJJ"
]



questions = [
    r"\question A car driver travels from the plains to the hill station, which are 200 km apart at an average speed of 40 km/hr. In the return trip, he covers the same distance at an average speed of 20 km/hr. What is the average speed of the car over the entire distance of 400 km?",
    r"\question Mac travels from A to B, a distance of 250 miles in 5.5 hours, and returns to A in 4.5 hours. What is his average speed?",
    r"\question A boy goes to his school from his house at a speed of 3 km/hr and returns at a speed of 2 km/hr. If he takes 5 hours in going and coming, what is the distance between his house and school?",
    r"\question The average speed of a train in the onward journey is 25% more than that in the return journey. The train halts for one hour at the destination. The total time taken for the complete to-and-fro journey is 17 hours, covering a distance of 800 km. What is the speed of the train in the onward journey?",
    r"\question A person starts on a bicycle at 7 a.m. to reach a certain place. After traveling a certain distance, the bicycle goes out of order, and he rests for 35 minutes before walking back home. He reaches home at 1 p.m. If his cycling speed is 10 km/hr and walking speed is 1 km/hr, how far did he cycle?",
    r"\question A, B, and C drive on a trip. A drives for 1 hour at an average speed of 50 km/hr, B for 2 hours at 48 km/hr, and C for 3 hours at 52 km/hr. What is their mean speed for the journey?",
    r"\question A man travels 160 km at 64 km/hr and the next 160 km at 80 km/hr. What is his average speed for the first 320 km of the tour?",
    r"\question A boy rides his bicycle 10 km at an average speed of 12 km/hr and then travels 12 km at an average speed of 10 km/hr. What is his average speed for the entire trip?",
    r"\question A man travels 600 km by train at 80 km/hr, 800 km by ship at 40 km/hr, 500 km by airplane at 400 km/hr, and 100 km by car at 50 km/hr. What is the average speed for the entire distance?",
    r"\question A car travels one-third of a distance at 10 km/hr, another third at 20 km/hr, and the last third at 60 km/hr. What is the average speed for the entire journey?",
    r"\question The speed of a car increases by 2 km/hr every hour. If the distance traveled in the first hour was 35 km, what was the total distance traveled in 12 hours?",
    r"\question A train covers a distance of 10 km in 12 minutes. If its speed decreases by 5 km/hr, how much time will it take to cover the same distance?",
    r"\question Anna left for city A from city B at 5:20 a.m., traveling at 80 km/hr for 2 hours 15 minutes, then reducing her speed to 60 km/hr. If the distance between the cities is 350 km, at what time did Anna reach city A?",
    r"\question An airplane covers a certain distance at 240 km/hr in 5 hours. What speed must it travel to cover the same distance in 3.5 hours?",
    r"\question A person covers a distance of 6 km in 45 minutes. If he covers half the distance in two-thirds of the total time, what must his speed be to cover the remaining distance in the remaining time?",
    r"\question A man performs half of his journey by rail, one-third by bus, and the remaining 6.5 km on foot. What is the total journey distance?",
    r"\question A person travels a journey in 10 hours. He travels the first half at 21 km/hr and the second half at 24 km/hr. What is the total journey distance?",
    r"\question A person travels equal distances at speeds of 3 km/hr, 4 km/hr, and 5 km/hr, taking a total of 47 minutes. What is the total distance?",
    r"\question A farmer travels a distance of 61 km in 9 hours, partly on foot at 4 km/hr and partly by bicycle at 9 km/hr. How far did he travel on foot?",
    r"\question A and B walk 24 km each. The sum of their speeds is 7 km/hr, and the total time taken by both is 14 hours. What is A's speed?",
    r"\question A person travels from P to Q at a speed of 40 km/hr and returns by increasing his speed by 50%. What is his average speed for the journey?",
    r"\question Which of the following speeds is the fastest: 25 m/sec, 90 km/hr, or 1500 m/min?",
    r"\question A person crosses a 600 m long street in 5 minutes. What is his speed in km/hr?",
    r"\question A man walking at 5 km/hr crosses a bridge in 15 minutes. What is the length of the bridge in meters?",
    r"\question How long will a boy take to run around a square field of side 35 meters if he runs at 9 km/hr?",
    r"\question A car is running at a speed of 108 km/hr. What distance will it cover in 15 seconds?",
    r"\question Two buses travel 300 km in 7.5 hours and 450 km in 9 hours, respectively. What is the ratio of their average speeds?",
    r"\question A truck covers 500 meters in 1 minute, and a bus covers 33 km in 45 minutes. What is the ratio of their speeds?",
    r"\question The speed ratio of two trains is 7:8. If the second train runs at 80 km/hr, what is the speed of the first train?",
    r"\question A train travels at an average speed of 70 miles per hour for 4 hours. How far did it travel?",
    r"\question A train passes 21 telephone poles in one minute, with poles 50 meters apart. At what speed is the train traveling?",
    r"\question Sound travels in air at 1100 ft/sec. A man hears an axe strike 11/5 seconds after seeing it. How far is the man from the chopper?",
    r"\question An express train travels at 100 km/hr, stopping for 3 minutes every 75 km. How long does it take to travel 600 km?",
    r"\question A cyclist and a jogger cover the same distance, with the cyclist taking half the time of the jogger. What is the ratio of their speeds?",
    r"\question A motorcar starts at 70 km/hr, increasing speed by 10 km/hr every two hours. How long does it take to cover 340 km?",
]


# Make sure the base output directory exists
os.makedirs(base_output_dir, exist_ok=True)

# Write each question to its own .tex file in a folder named after the corresponding code
for i, (code, question) in enumerate(zip(codes, questions)):
    # Create a folder for each code
    folder_path = os.path.join(base_output_dir, code)
    os.makedirs(folder_path, exist_ok=True)
    
    # Define the file path within that folder
    filename = os.path.join(folder_path, f"{code}.tex")
    
    # Generate the content for the LaTeX file with randomized choices
    content = (
    
        f"{question}" + "\n"
        r"\begin{randomizechoices}" + "\n"
        r"\choice --q1w1--" + "\n"
        r"\choice --q1w2--" + "\n"
        r"\choice --q1w3--" + "\n"
        r"\correctchoice --q1cc--" + "\n"
        r"\end{randomizechoices}" + "\n\n"
        
    )
    
    # Write the content to the file
    with open(filename, "w") as file:
        file.write(content)

print("All questions have been written to separate .tex files in their respective folders.")
