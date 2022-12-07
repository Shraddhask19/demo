#include <bits/stdc++.h>
using namespace std;

string RailFenceEncrypt(string text, int key)
{
    string result;
    char rail[key][text.length()];
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < text.length(); j++)
        {
            rail[i][j] = '\n';
        }
    }
    bool dir_down;
    int row = 0, col = 0;
    for (int i = 0; i < text.length(); i++)
    {
        if (row == 0)
            dir_down = true;
        else if (row == key - 1)
            dir_down = false;
        rail[row][col++] = text[i];
        if (dir_down)
            row++;
        else
            row--;
    }
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < text.length(); j++)
        {
            if (rail[i][j] != '\n')
                result.push_back(rail[i][j]);
        }
    }
    return result;
}

string RailFenceDecrypt(string ciphertext, int key)
{
    string result;
    char rail[key][ciphertext.length()];
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < ciphertext.length(); j++)
        {
            rail[i][j] = '\n';
        }
    }
    bool dir_down;
    int row = 0, col = 0;
    for (int i = 0; i < ciphertext.length(); i++)
    {
        if (row == 0)
            dir_down = true;
        else if (row == key - 1)
            dir_down = false;
        rail[row][col++] = '*';
        if (dir_down)
            row++;
        else
            row--;
    }
    int index = 0;
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < ciphertext.length(); j++)
        {
            if (rail[i][j] == '*' && index < ciphertext.length())
                rail[i][j] = ciphertext[index++];
        }
    }
    row = 0, col = 0;
    for (int i = 0; i < ciphertext.length(); i++)
    {
        if (row == 0)
            dir_down = true;
        else if (row == key - 1)
            dir_down = false;
        if (rail[row][col] != '*')
            result.push_back(rail[row][col++]);
        if (dir_down)
            row++;
        else
            row--;
    }
    return result;
}

int main()
{
    int option, key;
    string text, ciphertext;
    cout << "Enter option:\n1)Console\n2)File\n";
    cin >> option;
    cout << "Enter key: ";
    cin >> key;
    cin.ignore();
    switch (option)
    {
    case 1:
        cout << "Enter text: ";
        break;
    case 2:
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        break;
    }
    getline(cin, text);
    ciphertext = RailFenceEncrypt(text, key);
    cout << "Cipher Text: " << ciphertext << endl;
    cout << "Original Text: " << RailFenceDecrypt(ciphertext, key);
    return 0;
}
