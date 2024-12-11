module D_flip_flop(input logic clk, reset_b, input logic [7:0] d, output logic [7:0] q);
	always_ff @(posedge clk)
	begin
		if(reset_b) q <= 8'b00000000;
		else q <= d;
	end
endmodule

module part3(input logic Clock, Reset_b, input logic [3:0] Data, input logic [1:0] Function, output logic [7:0] ALU_reg_out);	
	logic [7:0] ALUout;	
	D_flip_flop u0(.clk(Clock), .reset_b(Reset_b), .d(ALUout), .q(ALU_reg_out));
	always_comb
	begin
		case (Function)
			0: ALUout = Data+ALU_reg_out[3:0];
			1: ALUout = Data*ALU_reg_out[3:0];
			2: ALUout = ALU_reg_out[3:0] << Data;
			3: ALUout = ALU_reg_out;
		endcase
	end
endmodule
	

