# Copyright (c) 2019, Łukasz Paszke. All rights reserved. see README for details.

class StringOutputBuffer(OutputBuffer)
    def join_elements(elements_list)
        joined_elements = ''
        for element in elements_list
            joined_elements = joined_elements + element
          
            
