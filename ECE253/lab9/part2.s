.global _start
_start:
    .equ LEDs, 0xFF200000
    .equ TIMER, 0xFF202000
    .equ PUSH_BUTTON, 0xFF200050
    .equ TOP_COUNT, 25000000

    li sp, 0x20000
    li a7, TOP_COUNT

    jal CONFIG_TIMER
    jal CONFIG_KEYS
    csrw mstatus, zero
    li t0, 0x10000
    li t1, 0x40000
    or t2, t0, t1
    csrw mie, t2
    la t2, interrupt_handler
    csrw mtvec, t2
    li t0, 0b1000
    csrw mstatus, t0

    la s0, LEDs
    la s1, COUNT
LOOP:
    lw s2, 0(s1)
    sw s2, 0(s0)
    j LOOP

interrupt_handler:
    addi sp, sp, -36
    sw t0, 0(sp)
    sw t1, 4(sp)
    sw t2, 8(sp)
    sw t3, 12(sp)
    sw t4, 16(sp)
    sw a0, 20(sp)
    sw a1, 24(sp)
    sw t5, 28(sp)
    sw t6, 32(sp)

    csrr t0, mcause
    li t1, 0x80000010
    beq t0, t1, timer_isr

    li t1, 0x80000012
    beq t0, t1, key_isr

    j interrupt_return

timer_isr:
    la t1, COUNT
    lw t2, 0(t1)
    la t3, RUN
    lw t4, 0(t3)
    add t2, t2, t4
    li t3, 255
    bgt t2, t3, reset_count
    sw t2, 0(t1)
    j clear_timer_interrupt

reset_count:
    li t2, 0
    sw t2, 0(t1)

clear_timer_interrupt:
    li t1, TIMER
    sw zero, 0(t1)
    j interrupt_return

key_isr:
    la t1, PUSH_BUTTON
    lw t2, 12(t1)
    bnez t2, key_action
    j interrupt_return

key_action:
    la t3, RUN
    lw t4, 0(t3)
    andi a1, t2, 0x1
    bnez a1, toggle_count
    andi a1, t2, 0x2
    bnez a1, double_speed
    andi a1, t2, 0x4
    bnez a1, halve_speed
    j interrupt_return

toggle_count:
    xori t4, t4, 1
    sw t4, 0(t3)
    j interrupt_return

double_speed:
    la t3, MAX_SPEED
    lw t4, 0(t3)
    ble a7, t4, no_change
    srli a7, a7, 1
    jal CONFIG_TIMER
    j interrupt_return

halve_speed:
    la t3, MIN_SPEED
    lw t4, 0(t3)
    bge a7, t4, no_change
    slli a7, a7, 1
    jal CONFIG_TIMER
    j interrupt_return

no_change:
j interrupt_return

interrupt_return:
    li t1, PUSH_BUTTON
    li t2, 0xF
    sw t2, 12(t1)

    lw t0, 0(sp)
    lw t1, 4(sp)
    lw t2, 8(sp)
    lw t3, 12(sp)
    lw t4, 16(sp)
    lw a0, 20(sp)
    lw a1, 24(sp)
    lw t5, 28(sp)
    lw t6, 32(sp)

    addi sp, sp, 36
    mret

CONFIG_TIMER:
    li t0, TIMER
    srli t2, a7, 16
    sw t2, 12(t0)
    li t3, 0x0000FFFF
    and t2, a7, t3
    sw t2, 8(t0)
    li t2, 0b0111
    sw t2, 4(t0)
    ret

CONFIG_KEYS:
    li t0, PUSH_BUTTON
    li t1, 0b0111
    sw t1, 8(t0)
    sw t1, 12(t0)
    ret

.data

MAX_SPEED:  .word 100
MIN_SPEED:  .word 100000000
COUNT:      .word 0x0
RUN:        .word 0x1
.end