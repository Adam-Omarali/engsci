module rate_divider
#(parameter CLOCK_FREQUENCY = 500)(input logic clk, reset, logic [1:0] speed, output logic en);
	logic [$clog2(CLOCK_FREQUENCY * 4) - 1:0] count;
	logic [$clog2(CLOCK_FREQUENCY * 4) - 1:0] counter;	
	always_comb
	begin
		if(speed == 2'b00) count = CLOCK_FREQUENCY;
		else if(speed == 2'b11) count = CLOCK_FREQUENCY * 4;
		else count = CLOCK_FREQUENCY * speed;
	end
	
	always_ff@(posedge clk)
	begin
		if(reset) 
		begin
			en <= 0;
			counter <= count - 1;
		end

		else if (counter == 'b0) 
		begin
			en <= 1'b1;
			counter <= count - 1;
		end

		else 
		begin
			counter <= counter - 1;
			en <= 1'b0;
		end
	end

endmodule


module display_counter(input logic enable, clk, reset, output logic [3:0] counter_value);
	always_ff@(posedge clk)
	begin
		if(reset) counter_value <= 'h0;
		else if(enable) counter_value = counter_value + 'h1;
	end
endmodule


module part2
#(parameter CLOCK_FREQUENCY = 500)(input logic ClockIn, Reset, logic [1:0] Speed, output logic [3:0] CounterValue);
	logic en;
	rate_divider u1(.clk(ClockIn), .reset(Reset), .speed(Speed), .en(en));
	display_counter u2(.enable(en), .clk(ClockIn), .reset(Reset), .counter_value(CounterValue));
endmodule
			