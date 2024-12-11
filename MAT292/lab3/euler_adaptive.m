function [T, Y] = euler_adaptive(f, t0, tN, y0, h)
    N = floor((tN - t0) ./ h); %N is the number of iterations. Don't use int32, conflicts with tan
    tol=1e-8;
    y = y0;
    t = t0;
    T = t0;
    Y = y0;
    while t < tN
        if t + h > tN
            h = tN - t;  % Adjust step size for the last step
        end
       
        y_onestep = y + h * f(t, y);
        y_halfstep_1 = y + h / 2 * f(t, y);
        z = y_halfstep_1 + h / 2 * f(t + h/2, y_halfstep_1);
        
        D = z - y_onestep;
        if abs(D) < tol
            t = t + h;
            y = z + D;
            T = [T, t];
            Y = [Y, y];
        end
        h = 0.9*h*min(max(tol/abs(D),0.3),2);
    end
end