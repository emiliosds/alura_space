from django import forms

class CadastrarForms(forms.Form):
    nome=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )

    email=forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )

    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )

    confirmacao_senha=forms.CharField(
        label='Confirme sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Por favor, não insira espaço no nome do usuário.")
            else:
                return nome

    def clean_confirmacao_senha(self):
        senha = self.cleaned_data.get("senha")
        confirmacao_senha = self.cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha:
            if senha != confirmacao_senha:
                raise forms.ValidationError("Senha diferente da confirmação de senha.")
            else:
                return senha