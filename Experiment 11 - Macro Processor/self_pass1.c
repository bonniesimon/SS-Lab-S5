#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(){
    char label[20], opnd[20], mne[20];
    FILE *inp, *namtab, *deftab;
    inp = fopen("inp_self.txt", "r");
    namtab = fopen("namtab_self.txt", "w+");
    deftab = fopen("deftab_self.txt", "w+");

    fscanf(inp, "%s%s%s", label, mne, opnd);
    while(strcmp(mne, "MEND") != 0){
        if(strcmp(mne, "MACRO") == 0){
            fprintf(namtab, "%s\n", label);
            fprintf(deftab, "%s\t%s\n", label, opnd);
        }else{
            fprintf(deftab, "%s\t%s\n", mne, opnd);
        }
        fscanf(inp, "%s%s%s", label, mne, opnd);
    }
    fprintf(deftab, "%s", mne);
    fclose(inp);
    fclose(namtab);
    fclose(deftab);
    printf("\nPass 1 Completed\n");
}