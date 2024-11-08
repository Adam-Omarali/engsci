vlib work 
vlog part3.sv
vsim part3

log {/*}
#adding individual waves
add wave {/*}

#clock signal
force Clock 0, 1 1ns -r 2ns

#reset first
force Reset 1
force Go 0 
force Divisor 5'b00011
force Dividend 4'b0111
run 2ns
force Reset 0 
force Go 1
run 1ns

force Go 0

run 14ns

force Go 1

run 2ns

force Go 0

run 14ns
