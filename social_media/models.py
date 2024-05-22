from django.db import models
from django.urls import reverse
from users.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    image = models.ImageField(upload_to="media/posts/images/", blank=True)
    video = models.FileField(upload_to="media/posts/videos/", blank=True)
    creat_time = models.DateTimeField(auto_now_add=True)
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ["-creat_time"]  # Default ordering by latest posts first

    def __str__(self):
        if self.content:
            return f"{self.user.name}: {self.content[:25]}..."  # Truncated content for list displays
        else:
            if self.image:
                return f"{self.user.name}: Image Post"
            elif self.video:
                return f"{self.user.name}: Video Post"
            else:
                return f"{self.user.name}: Empty Post"

    def like(self):
        self.like_count += 1
        self.save()

    def remove_like(self):
        if self.like_count > 0:
            self.like_count -= 1
            self.save()

    def add_comment(self):
        self.comment_count += 1
        self.save()

    def remove_comment(self):
        if self.comment_count > 0:
            self.comment_count -= 1
            self.save()


class Comment(models.Model):
    content = models.TextField(max_length=1024)
    created_time = models.DateTimeField(auto_now_add=True)
    like_count = models.PositiveIntegerField(default=0)
    inner_comment_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return f"{self.user.name} on {self.post.id}: {self.content[:25]}..."

    def like(self):
        self.like_count += 1
        self.save()

    def remove_like(self):
        if self.like_count > 0:
            self.like_count -= 1
            self.save()

    def add_inner_comment(self):
        self.inner_comment_count += 1
        self.save()

    def remove_inner_comment(self):
        if self.inner_comment_count > 0:
            self.inner_comment_count -= 1
            self.save()


class InnerComment(models.Model):
    content = models.TextField(max_length=1024)
    created_time = models.DateTimeField(auto_now_add=True)
    like_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="inner_comments"
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="inner_comments"
    )

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return f"{self.user.name} on {self.comment.id}: {self.content[:25]}..."

    def like(self):
        self.like_count += 1
        self.save()

    def remove_like(self):
        if self.like_count > 0:
            self.like_count -= 1
            self.save()