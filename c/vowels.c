// Reads a word, checks each character against the vowels case-insensitively, counts the matches, and prints the total (example: "Education" -> 5).

#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char word[1000];
    int count = 0;

    scanf("%999s", word);

    for (int i = 0; word[i] != '\0'; i++) {
        char c = word[i];

        c = tolower(c);

		if (c == 'a' || c == 'e' || c == 'i' ||
		    c == 'o' || c == 'u')
		{
		    count++;
		}
    }

    printf("%d\n", count);

    return 0;
}
