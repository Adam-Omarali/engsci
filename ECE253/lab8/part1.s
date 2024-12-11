.global _start
_start:
	li s1, 0xFF200000 #address of leds
	li s0, 0xFF200050 #addres of keys
	li s6, 15
	li s7, 1
	mv s4, zero
	POLL: 
		lw s2, 0(s0)
		beqz s2, POLL
		
	WAIT: 
		lw s3, 0(s0)
		bnez s3, WAIT #if not zero, go back to WAIT, what if only one key is zero?
		li s3, 1
		addi s5, s2, 0x1
		bne s5, s3, CHECK_1
		beqz s4, AFTER_3
		#key zero has been pressed
		li s4, 1
		j UPDATE_LED
	CHECK_1:
		li s3, 2 #0b0010
		and s5, s2, s3 #ex - 2: 0b0110 -> 0b0010
		bne s5, s3, CHECK_2
		beq s4, s6, UPDATE_LED #break if at max value
		beqz s4, AFTER_3
		addi s4, s4, 1 #add 1
		j UPDATE_LED
	CHECK_2:
		li s3, 4
		and s5, s2, s3
		bne s5, s3, CHECK_3
		beq s4, s7, UPDATE_LED #break if at min value
		beqz s4, AFTER_3
		addi s4, s4, -1
		j UPDATE_LED
	CHECK_3:
		mv s4, zero
		
	AFTER_3:
		li s4, 1
		
		
	UPDATE_LED:
		sw s4, 0(s1)
		j POLL
	
	