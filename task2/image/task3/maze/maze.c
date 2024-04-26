#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdlib.h>


 
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

typedef struct {
    unsigned char r, g, b;
} Pixel;

Pixel** read_bmp(const char* filename, int* width, int* height, int* filesize) {
    FILE* f = fopen(filename, "rb");
    if (!f) {
        printf("Error opening file.\n");
        return NULL;
    }

    unsigned char header[54];
    fread(header, sizeof(unsigned char), 54, f);

    *filesize = *(int*)&header[2];
    *width = *(int*)&header[18];
    *height = *(int*)&header[22];

    int padding = (4 - (*width * 3) % 4) % 4;

    Pixel** pixels = (Pixel**)malloc(*height * sizeof(Pixel*));
    for (int i = 0; i < *height; i++) {
        pixels[i] = (Pixel*)malloc(*width * sizeof(Pixel));
    }

    for (int i = 0; i < *height; i++) {
        for (int j = 0; j < *width; j++) {
            fread(&pixels[i][j], sizeof(Pixel), 1, f);
        }
        fseek(f, padding, SEEK_CUR);
    }

    fclose(f);
    return pixels;
}

void write_first_32_bytes(const char* filename, Pixel** pixels, int width, int height) {
    FILE* f = fopen(filename, "wb");
    if (!f) {
        printf("Error opening file.\n");
        return;
    }

    int count = 0;
    for (int i = height - 1; i >= 0 && count < 32; i--) {
        for (int j = 0; j < width && count < 32; j++) {
            if (pixels[i][j].r == pixels[i][j].g && pixels[i][j].g == pixels[i][j].b) {
                fwrite(&pixels[i][j], 1, 1, f);
                count++;
                if (count == 32) goto _metka;
            }
        }
    } 
    _metka:

    fclose(f);
}

unsigned char* find(int height, int width,  unsigned int mas_weight[height][width]){
    int cost[height][width];
	int pred[height][width];

	cost[0][0] = mas_weight[0][0];
	for (int c = 1; c < height; ++c) {
		cost[0][c] = cost[0][c-1] + mas_weight[0][c];
		pred[0][c] = 1;
	}
	for (int r = 1; r < width; ++r) {
		cost[r][0] = cost[r-1][0] + mas_weight[r][0];
		pred[r][0] = 0;
		for (int c = 1; c < height; ++c) {
			if (cost[r-1][c] < cost[r][c-1]) {
				cost[r][c] = mas_weight[r][c] + cost[r-1][c];
				pred[r][c] = 0;
			}
			else {
				cost[r][c] = mas_weight[r][c] + cost[r][c-1];
				pred[r][c] = 1;
			}
		}
	}
    printf("sum: %d\n", cost[width-1][height-1]);

    unsigned char *key = (unsigned char*)malloc(32);
    memset(key, 0, 32);
    key[0] = cost[width-1][height-1] % 256;
    int c = height - 1;
	int r = width - 1;
    for(;;) {
		printf("%d %d %d %d\n", mas_weight[r][c], r, c, pred[r][c]);
		if (pred[r][c]){
			--c;
		}	
	 	else {
			--r;
		}
		if (c + r < 31) {
			key[c+r+1] = mas_weight[r][c];
		}
		if (c == 0 && r == 0)break;
	}

    return key;
}



int main() {
    int width, height, filesize;
    Pixel** bmp_data = read_bmp("task.bmp", &width, &height, &filesize);
    if (!bmp_data) return 1;
    
    unsigned int mas_weight[height][width];
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            // printf("%d %d\n", i, j);
            mas_weight[i][j] = bmp_data[height-i-1][j].r + bmp_data[height-i-1][j].g + bmp_data[height-i-1][j].b;
            // printf("%d ", mas_weight[i][j]);
        }
        // printf("\n");
    } 
    printf("height: %d \nwidht: %d\n", height, width);
    
    unsigned char *key;
    key = find(height, width, mas_weight);
    puts("\n");
    for (int i = 0; i < 32; i++)
        printf("%d ", key[i]);
    FILE* f = fopen("key", "wb");
    fwrite(key, 1, 32, f);
    fclose(f);



    // write_first_32_bytes("key", bmp_data, width, height);
    // for (int i = 0; i < height; i++) {
    //     free(bmp_data[i]);
    // }
    free(bmp_data);
    bmp_data = NULL;

    return 0;
}