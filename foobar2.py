def answer(l):
    # your code here

    def get_details(elevator):

        details = [None,None,None]
        detail_index = 0
        detail = ''
       
        last_dot = 0
        for i in range(0,len(elevator)):
            if elevator[i] != '.':
                detail += elevator[i]
            else:
                details[detail_index] = int(detail)
                detail_index += 1
                detail = ''
                last_dot = i+1
        
        details[detail_index] = int(elevator[last_dot:len(elevator)])
        return details
            
    def compare(elevator1,elevator2):
        elevator1_details = get_details(elevator1)
        elevator2_details = get_details(elevator2)
        
        for i in range(0,len(elevator1_details)):
            if elevator1_details[i] is None and elevator2_details[i] is not None:
                return -1
            
            if elevator1_details[i] is not None and elevator2_details[i] is None:
                return 1
            
            if elevator1_details[i] > elevator2_details[i]:
                return 1
              
            if elevator2_details[i] > elevator1_details[i]:
                return -1
           
        return 0
    
    return sorted(l,cmp=compare)


print answer(['3','2.0','3.1','1.0.5'])



print answer(['2.0.0','2.0','2.1.2','2.1.1', '2.0.1', '2.3', '1.0','1','1.0.0', '2.0.0', '2'])
