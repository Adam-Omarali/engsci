module control_path(input logic Clock, Reset, Go, output logic run, ResultValid);

typedef enum logic [3:0]
{
    C0 = 'd0,
    C1 = 'd1, 
    C2 = 'd2,
    C3 = 'd3,
    C4 = 'd4
} statetype;

statetype current_state, next_state;


// control FSM state table
always_comb begin
    run = 0;
    case(current_state)
	C0: begin
		if (Go) begin
			run = 1;
			next_state = C1;
		end else next_state = C0;
	end
        C1: next_state = C2;
	C2: next_state = C3;
	C3: next_state = C4;
	C4: next_state = C0;
    endcase
end

always_ff @(posedge Clock) begin
	if(Reset | Go) ResultValid = 0;
	else if (current_state == C4) ResultValid = 1'b1;
end

// control FSM FlipFlop
always_ff @(posedge Clock) begin
    if(Reset)
        current_state <= C0;
    else
       current_state <= next_state;
end



endmodule

module datapath(input logic Clock, Reset, Go, ResultValid, logic [4:0] Divisor, logic [3:0] Dividend,
		output logic [3:0] Quotient, dividend_out, div_in, div_shift, logic [4:0] Remainder, A, A_out, A_shift, A_temp);

//Dividend FF
always_ff @(posedge Clock)
begin
	if (Reset | Go) dividend_out <= Dividend;
	else if (~ResultValid) dividend_out <= div_in;
end

//A FF
always_ff @(posedge Clock)
begin
	if (Reset | Go) A <= 0;
	else if (~ResultValid) A <= A_out;
end

//shift
always_comb
begin
	A_shift = A << 1;
	A_shift = {A_shift[4:1], dividend_out[3]};
	div_shift = dividend_out << 1;
end

//ALU 1: Subtract Divisor from A
always_comb
begin
	A_temp = A_shift - Divisor;
	if (A_temp[3] == 1'b1) begin
		A_out = A_shift;
		div_in = {div_shift[3:1], 1'b0};
	end
	else begin
		div_in = {div_shift[3:1], 1'b1};
		A_out = A_temp;
	end
end

assign Remainder = ResultValid ? A : 5'bx;
assign Quotient = ResultValid ? dividend_out : 5'bx;


endmodule


module part3(input logic Clock, Reset, Go, logic [4:0] Divisor, logic [3:0] Dividend, 
	     output logic [3:0] Quotient, logic [4:0] Remainder, logic ResultValid);
	
	logic run;
	logic [4:0] A;
	logic [3:0] dividend_out, div_in, div_shift;
	logic [4:0] A_out, A_shift, A_temp;
	

	control_path u1(.Clock(Clock), .Reset(Reset), .Go(Go), .run(run), .ResultValid(ResultValid));
	datapath u2 (.Clock(Clock), .Reset(Reset), .Go(run), .ResultValid(ResultValid), .Divisor(Divisor), .Dividend(Dividend), .Quotient(Quotient), .Remainder(Remainder), .A(A),
		     .dividend_out(dividend_out), .div_in(div_in), .div_shift(div_shift), .A_out(A_out), .A_shift(A_shift), .A_temp(A_temp));
	

endmodule