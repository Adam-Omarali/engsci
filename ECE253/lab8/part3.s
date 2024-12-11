.equ PERIOD, 25000000
.equ TIMER, 0xFF202000
.equ LEDR, 0xFF200000

.global _start
_start:

la s7, LEDR
li t0, TIMER
li t1, PERIOD
la s6, 0xFF20005C #edgecapture
la s5, 0xFF200050 


li a1, 0x0000FFFF

li s8, 255

and a3, a1, t1
srli a4, t1, 16
sw a3, 8(t0)
sw a4, 12(t0)

li t3, 6
sw t3, 4(t0)

RESET:
	mv a0, zero

UPDATE:
	addi a0, a0, 1
	ble s8, a0, RESET

jal SET_LEDS

SUB_LOOP:
	lw s10, 0(t0)
	andi s10, s10, 1
	lw s9, 0(s5)
	beqz s9, CONTINUE
POLL:	
	lw s9, 0(s5)
	bnez s9, POLL
	lw t2, 0(t0) 
	andi t4, t2, 2
	beqz t4, START
	li t3, 8
	sw t3, 4(t0)
CONTINUE:
	beqz s10, SUB_LOOP
	li t5, 2
	sw t5, 0(t0)
	j UPDATE
	
START:
	li t3, 6
	sw t3, 4(t0)
	j SUB_LOOP

SET_LEDS:
	sw a0, 0(s7)
	jr ra


.global LIST
.data
Timer:
.word 0x00005
max:
.word 0xffffffff
edge:
.word 0xFF20005C