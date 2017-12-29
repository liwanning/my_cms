
'''
create some records for demo database
'''

from perfect_CMS.wsgi import *
from cms.models import Category, Story,User


def main():
    Cty_urls = [
      ('体育新闻', 'sports'),
      ('社会新闻', 'society'),
      ('科技新闻', 'tech'),
    ]
    user = User.objects.first()
    for column_name, url in Cty_urls:
        c = Category.objects.get_or_create(label=column_name, slug=url)[0]

        # 创建 10 篇新闻
        for i in range(1, 11):
            article = Story.objects.update_or_create(
                title='{}_{}'.format(column_name, i),
                slug='article-{}-{}'.format(url,i),
                category = c,
                owner = user,
                makedown_content='新闻详细内容： {} {}'.format(column_name, i)
            )[0]




if __name__ == '__main__':
    main()
    print("Done!")