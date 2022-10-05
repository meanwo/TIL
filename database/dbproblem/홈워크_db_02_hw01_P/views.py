@ require_POST
def comment_create(request, article_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = article
        comment.article = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

