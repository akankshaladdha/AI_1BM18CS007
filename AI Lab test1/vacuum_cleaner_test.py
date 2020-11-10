location = [0,1]
                                                                            
def clean(location):
    vc_pos = 0
    last_pos = 0

    if sum(location)==0:
        print("Cleaned")    
    while(sum(location)>0):
        if location[vc_pos]== 1:
            if vc_pos == 0:
                last_pos = 0
                print("Position left cleaned ")
                
            else:
                last_pos = 1
                print("Position right cleaned")

            if vc_pos == 1:
                if last_pos == 0:
                    print("Cleaned area")
                    break
                else:
                    vc_pos = 0

            if vc_pos == 0:
                if last_pos == 1:
                    print("cleaned area")
                    break
                else:
                    vc_pos = 1

        else:
            if vc_pos == 0:
                print("left  position is already cleaned")
                if last_pos == 1:
                    print("cleaned area")
                    break
                else:
                    vc_pos = 1
                    continue

            if vc_pos == 1:
                print("right position is already cleaned")
                if last_pos == 0:
                    print("cleaned area")
                    break
                else:
                    vc_pos = 0

def main():
    location = list(map(int,input("Specify state of left and right side of environment\n").split(" ")))
    clean(location)

main()
                

            
            
