def answer(area):
    # your code here    
    answer = []
    
    while (area != 0):
        lowest_index=1 # lowest possible square root
        highest_index=1000 # highest possible square root

 
        while ((lowest_index != highest_index) and (highest_index - 1 != lowest_index)):
            if area == highest_index**2:
                answer.append( ((highest_index))**2 )
                return answer
            
            if area == lowest_index**2:
                answer.append( (lowest_index)**2)
                return answer

            if area < (( ( lowest_index + highest_index ) / 2 )**2):
                highest_index = (( lowest_index + highest_index ) / 2 )
            elif area > ( (lowest_index + highest_index)/2 **2):
                lowest_index = ((lowest_index + highest_index)/2)
                            
        if lowest_index == highest_index:
            answer.append(lowest_index**2)
            area -= lowest_index**2
        else:
            if highest_index**2 <= area:
                area -= highest_index**2
                answer.append(highest_index**2)
            if lowest_index**2 <= area:
                area -= lowest_index**2
                answer.append(lowest_index**2)

    return answer
