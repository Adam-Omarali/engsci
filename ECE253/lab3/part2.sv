module part2(input logic [3:0] A, B, input logic [1:0] Function, output logic [7:0] ALUout);
	logic [3:0] s;
	logic cout;
	part1 v1(.a(A), .b(B), .c_in(0), .s(s), .c_out(cout));
	
	always_comb
	begin
		case (Function)
			0: ALUout = {3'b000, cout, s};
			1: ALUout = (|A)|(|B) ? 8'b00000001 : 8'b00000000;
			2: ALUout = (&A)&(&B) ? 8'b00000001 : 8'b00000000;
			3: ALUout = {A, B};
		endcase
	end

endmodule

module mux2to1(input logic x, y, s, output logic o);
    always_comb
	begin
	    if(s == 0) o = x;
	    else o = y;
	end
endmodule


module FA(input logic a, b, cin, output logic s, cout);
	logic w2;
	assign w2 = a ^ b;
	mux2to1 u0(.x(b), .y(cin), .s(w2), .o(cout));
	assign s = w2 ^ cin;
endmodule
	
module part1(input logic [3:0] a, b, input logic c_in, output logic [3:0] s, c_out);
	FA u0(.a(a[0]), .b(b[0]), .cin(c_in), .cout(c_out[0]), .s(s[0]));
	FA u1(.a(a[1]), .b(b[1]), .cin(c_out[0]), .cout(c_out[1]), .s(s[1]));
	FA u2(.a(a[2]), .b(b[2]), .cin(c_out[1]), .cout(c_out[2]), .s(s[2]));
	FA u3(.a(a[3]), .b(b[3]), .cin(c_out[2]), .cout(c_out[3]), .s(s[3]));
endmodule
	