from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Model form for the site owner to create,
    edit and delete wizard battle posts.
    """
    class Meta:
        model = Post
        fields = ('title', 'text_content', 'image_one', 'image_two',)

        def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super().form_valid(form)


class CommentForm(forms.ModelForm):
    """
    Model form for users to leave a comment on a wizard battle post.
    """
    class Meta:
        model = Comment
        fields = ('comment_body', 'name',)
