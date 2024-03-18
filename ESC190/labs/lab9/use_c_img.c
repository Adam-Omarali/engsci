#include "c_img.c"

void make_img_brighter(struct rgb_img *im, double brightness, char *filename){
    for (int i = 0; i < im->height; i++){
        for (int j = 0; j < im->width; j++){
            int r = (int) (get_pixel(im, i, j, 0) * brightness);
            int g = (int) (get_pixel(im, i, j, 1) * brightness);
            int b = (int) (get_pixel(im, i, j, 2) * brightness);
            if (r > 255)
                r = 255;
            if (g > 255)
                g = 255;
            if (b > 255)
                b = 255;
            set_pixel(im, i, j, r, g, b);
        }
    }
    write_img(im, filename);
}

int main()
{
    struct rgb_img *im;
    create_img(&im, 300, 300);
    read_in_img(&im, "img/image.bin");

    make_img_brighter(im, 1, "img/bright.bin");
    make_img_brighter(im, 1.5, "img/brighter.bin");
    make_img_brighter(im, 2, "img/brightest.bin");
    make_img_brighter(im, 0.9, "img/dark.bin");
    make_img_brighter(im, 0.6, "img/darker.bin");
    make_img_brighter(im, 0.4, "img/darkest.bin");

    destroy_image(im);

}