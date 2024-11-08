vlib work

# compile all system verilog modules in mux.sv to working dir
# could also have multiple verilog files
vlog part1.sv

#load simulation using mux as the top level simulation module
vsim part1

#log all signals and add some signals to waveform window
log {/*}
# add wave {/*} would add all items in top level simulation module
add wave {/*}


force {Clock} 0 0ns, 1 {5ns} -r 10ns

force {Reset} 1'b1
force {w} 1'b0
run 10ns

force {Reset} 1'b0
force {w} 1'b1
run 10ns

force {Reset} 1'b0
force {w} 1'b1
run 10ns

force {Reset} 1'b0
force {w} 1'b1
run 10ns

force {Reset} 1'b0
force {w} 1'b1
run 10ns

force {Reset} 1'b0
force {w} 1'b0
run 10ns

force {Reset} 1'b0
force {w} 1'b1
run 10ns

force {Reset} 1'b0
force {w} 1'b1
run 10ns