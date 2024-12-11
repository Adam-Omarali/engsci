.global _start
.text
_start:
	la s0, LIST # num of elements
	lw s1, 0(s0) #counter (i loop)
	addi s1, s1, 0
	addi s0, s0, 4 #move to first word
	LOOP1:
		addi s1, s1, -1
		blt s1, zero, END
		mv s2, zero#counter (j loop)
		#need to move s0 back to start, s1 iterations
		
		LOOP2:
			bge s2, s1, ENDLOOP2
			jal SWAP
		NEXT:
			addi s0, s0, 4
			addi s2, s2, 1
			j LOOP2
		ENDLOOP2:
			li t3, -4
			mul t3, t3, s1
			add s0, s0, t3
			j LOOP1
			
SWAP:
	lw t0, 0(s0)
	lw t1, 4(s0)
	bgt t0, t1, CHANGE
	j NEXT
	
	CHANGE:
		sw t1, 0(s0)
		sw t0, 4(s0)
	jr ra
	
END: j END

.global LIST
.data
LIST:
.word 3, 7, 5, 3