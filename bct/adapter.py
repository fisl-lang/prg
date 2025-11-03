
import sys

size = 3

while True:
    line = sys.stdin.readline().replace("\n", "")

    #finite state machine, cuz i'm chill like that.
    #it will match sentences like (100)^n,
    #and while doing so, count the n.
    state = "s0"
    count = 0 
    for char in line + '\0':
        match state:
            case "s0" if char == "1":  state = "s1"
            case "s0" if char == "0":  state = "reject"
            case "s0" if char == "\0": state = "accept"

            case "s1" if char == "0":  state = "s2"
            case "s1" if char == "1":  state = "reject"
            case "s1" if char == "\0": state = "reject"

            case "s2" if char == "0":
                state = "s0"
                count += 1
            case "s2" if char == "1":  state = "reject"
            case "s2" if char == "\0": state = "reject"
            
    if state == "accept":
        print(count, flush=True)

