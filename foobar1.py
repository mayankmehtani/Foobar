def answer(area):
    # your code here    
    return_list = []
    
    while (area != 0):

        lowest_index=1
        highest_index=1000

        while ((lowest_index != highest_index) and (highest_index - 1 != lowest_index)):
            if area == highest_index**2:
                return_list.append( ((highest_index))**2 )
                return return_list
            
            if area == lowest_index**2:
                return_list.append( (lowest_index)**2)
                return return_list

            if area < (( ( lowest_index + highest_index ) / 2 )**2):
                highest_index = (( lowest_index + highest_index ) / 2 )
            elif area > ( (lowest_index + highest_index)/2 **2):
                lowest_index = ((lowest_index + highest_index)/2)
                            
        if lowest_index == highest_index:
            return_list.append(lowest_index**2)
            area -= lowest_index**2
        else:
            if highest_index**2 <= area:
                area -= highest_index**2
                return_list.append(highest_index**2)
            if lowest_index**2 <= area:
                area -= lowest_index**2
                return_list.append(lowest_index**2)

    return return_list