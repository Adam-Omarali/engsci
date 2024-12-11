.global _start
.text

_start:
	la s2, LIST
	addi s10, zero, 0 #sum
	addi s11, zero, 0 #len
	
	addi s5, zero, -1

	#curr_item
	lb s4, 0(s2)
	LOOP: 
		beq s4, s5, END
		add s10, s10, s4 #add curr item
		addi s11, s11, 1 #increment len
		addi s2, s2, 4
		lb s4, 0(s2) #load next item in list
		j LOOP
	
	
	
END: j END

.global LIST
.data
LIST:
.word 1, 2, 3, 5, 0xA, -1
	