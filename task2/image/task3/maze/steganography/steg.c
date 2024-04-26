#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define FILE_A "a.bmp"
#define FILE_B "b.bmp"

#define HDR_SIZE 54

int main(){
  int width, height, filesize;

  uint8_t *hdr = (uint8_t*)malloc(HDR_SIZE);
  int fd_a = open("a.bmp", O_RDONLY);
  int fd_b = open("b.bmp", O_RDONLY);
  int fd_out = open("out.bmp", O_WRONLY | O_CREAT | O_TRUNC, 0644);
  if (fd_out == -1 || fd_a == -1 || fd_b == -1) {
      perror("open");
      return -1; 
  }

  read(fd_a, hdr, HDR_SIZE);
  lseek(fd_b, HDR_SIZE, SEEK_SET);

  filesize = *(int*)&hdr[2];
  height = *(int*)&hdr[18] * 3;
  width = *(int*)&hdr[22] * 3;

  printf("%d %d %d\n", width, height, filesize);
  filesize -= HDR_SIZE;
  write(fd_out, hdr, HDR_SIZE);
  lseek(fd_out, HDR_SIZE, SEEK_SET);

  uint8_t *bmp_data_a = (uint8_t*)malloc(filesize);
  uint8_t *bmp_data_b = (uint8_t*)malloc(filesize);
  memset(bmp_data_a, 0, filesize);
  memset(bmp_data_b, 0, filesize);
  uint8_t bmp_data_c[filesize];

  read(fd_a, bmp_data_a, filesize);
  read(fd_b, bmp_data_b, filesize);

  for (int i = 0; i < filesize; i++)
    bmp_data_c[i] = (bmp_data_a[i]%2 + bmp_data_b[i]%2)*127;

  write(fd_out, bmp_data_c, filesize);

  close(fd_a);
  close(fd_b);
  close(fd_out);

  free(bmp_data_a);
  free(bmp_data_b);


  // for (int i = 0; i < height; i++){
  //   for (int j = 0; j < width; j++){
  //     bmp_data_c[i*j+1];
  //   }
  // }

  // int fd_out = open("out.bmp", O_WRONLY);
  // write(fd_out, hdr, HDR_SIZE);

  






}