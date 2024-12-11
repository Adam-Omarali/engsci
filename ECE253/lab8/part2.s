.global _start
_start:

la s7, 0xFF200000 #leds
la s6, 0xFF20005C #edgecapture
la s5, 0xFF200050 
addi s8, zero, 255


RESET: mv a0, zero


UPDATE:
	addi a0, a0, 1
	ble s8, a0, RESET

jal SET_LEDS

lw s10, 0(s6)
beqz s10, DO_DELAY
j POLL

DO_DELAY:
	la s1, Timer
	lw s0, 0(s1)


SUB_LOOP:
	addi s0, s0, -1
        bnez s0, SUB_LOOP
	j UPDATE

SET_LEDS:
	sw a0, 0(s7)
	jr ra

POLL:
	lw s9, 0(s5)
	beqz s9, POLL
POLL_2:
	lw s11, 0(s5)
	beqz s11, NEXT
	j POLL_2
NEXT:
	li s4, 0xFFFF
	sw s4, 0(s6)
	j UPDATE

.global LIST
.data
Timer:
.word 2500000
max:
.word 0xffffffff
edge:
.word 0xFF20005C