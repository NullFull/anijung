from django.db import models as m


class Company(m.Model):
    name = m.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name}'


class Judge(m.Model):
    name = m.CharField(max_length=20)
    company = m.ForeignKey(Company, null=True, on_delete=m.CASCADE)
    position = m.CharField(max_length=40)  # TODO : 이 아이도 별도 모델로

    class Meta:
        verbose_name = '판사'
        verbose_name_plural = '판사'
        
    def __str__(self):
        return self.name


class Case(m.Model):
    title = m.CharField(max_length=200)
    desc = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name = '사건'
        verbose_name_plural = '사건'

    def __str__(self):
        return self.title


class Decision(m.Model):
    no = m.CharField(max_length=20)
    case = m.ForeignKey(Case, on_delete=m.CASCADE, null=True, related_name='decisions')
    court = m.CharField(max_length=30)  # TODO : 이 아이도 별도 모델로
    place = m.CharField(max_length=20)  # TODO : 위 아이랑 묶어서 별도 모델로
    round = m.CharField(max_length=20)
    result = m.TextField()
    source = m.URLField(null=True)
    judge = m.ForeignKey(Judge, related_name='decisions', on_delete=m.CASCADE, null=True)  # TODO : 여러 판사 지원
    # judges = m.ManyToManyField(Judge, related_name='decisions')

    class Meta:
        verbose_name = '판결'
        verbose_name_plural = '판결'
    
    def __str__(self):
        return f'{self.case.title} - {self.round} - {self.result}'


class Quote(m.Model):
    # case = m.ForeignKey(Case, on_delete=m.CASCADE, null=True, blank=True)
    decision = m.ForeignKey(Decision, on_delete=m.CASCADE, null=True, blank=True)
    quote = m.CharField(max_length=300)
    source = m.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.quote}'
