function y = heun(f, t0, tN, y0, h)
    N = floor((tN - t0) ./ h); %N is the number of iterations. Don't use int32, conflicts with tan
    y = zeros(1, N);
    y(1) = y0;
    for i=1:N
        curr_slope = f(t0 + h * (i - 1), y(i));
        next_slope = f(t0 + h * (i), y(i) + h * curr_slope);
        y(i + 1) = y(i) + h / 2 * (curr_slope + next_slope);
    end
end