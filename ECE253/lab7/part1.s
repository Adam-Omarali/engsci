# Program that counts consecutive 1’s.
.global _start
.text
_start:
	la a2, LIST # Load the memory address into a2, the address are different than words
	addi t4, zero, 0 # Register t4 will hold the result
	addi s5, zero, -1
	add s10, zero, zero
	jal ONES
	add s10, zero, t4 #max ones

ONES:
	LOOP1:
		lw t3, 0(a2) #load curr word
		lw t5, 0(a2) #for shifting
		mv t6, zero
		beq t3, s5, RET #if curr -1, go to ret
		
		LOOP2: #find longest # ones in curr word
			beqz t3, MAX # Loop until data contains no more 1’s
				srli t5, t3, 1 # Perform SHIFT, followed by AND
				and t3, t3, t5
				addi t6, t6, 1 # Count the string lengths so far
				j LOOP2
				
		MAX:
			#max
			bgt t6, t4, CHANGE
			j NEXT
		CHANGE:
			mv t4, t6
		NEXT:
			addi a2, a2, 4 #move to next word
			j LOOP1	
			
	RET:
		jr ra

END: j END
.global LIST
.data
LIST:
.word 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x103fe00f, 0x00000005, 0x00000006, 0x00000007, 0x00000008, 0x00000009, -1
