module D_flip_flop(input logic clk, reset_b, d, output logic Q);
	always_ff @(posedge clk)
	begin
		if(reset_b) Q <= 0;
		else Q <= d;
	end
endmodule

module part1a(input logic LoadLeft, right, left, data, ParallelLoadn, clock, reset, output logic Q);
	logic mux1out, mux2out;
	assign mux1out = LoadLeft ? left : right;
	assign mux2out = ParallelLoadn ? mux1out : data;
	D_flip_flop u0(.clk(clock), .reset_b(reset), .d(mux2out), .Q(Q));
endmodule

module part1(input logic clock, reset, ParallelLoadn, RotateRight, ASRight, input logic [3:0] Data_IN, output logic [3:0] Q);
	logic wire1;
	assign wire1 = ASRight ? Q[3] : Q[0];
	part1a u0(.right(Q[3]), .left(Q[1]), .data(Data_IN[0]), .ParallelLoadn(ParallelLoadn), .LoadLeft(RotateRight), .clock(clock), .reset(reset), .Q(Q[0]));
	part1a u1(.right(Q[0]), .left(Q[2]), .data(Data_IN[1]), .ParallelLoadn(ParallelLoadn), .LoadLeft(RotateRight), .clock(clock), .reset(reset), .Q(Q[1]));
	part1a u2(.right(Q[1]), .left(Q[3]), .data(Data_IN[2]), .ParallelLoadn(ParallelLoadn), .LoadLeft(RotateRight), .clock(clock), .reset(reset), .Q(Q[2]));
	part1a u3(.right(Q[2]), .left(wire1), .data(Data_IN[3]), .ParallelLoadn(ParallelLoadn), .LoadLeft(RotateRight), .clock(clock), .reset(reset), .Q(Q[3]));
endmodule



