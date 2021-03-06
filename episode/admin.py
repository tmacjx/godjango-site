from django.contrib import admin
from models import Video, Category


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'admin_thumbnail', 'title', 'admin_link', 'publish_date', 'is_premium')
    list_display_links = ('admin_thumbnail', 'title')
    exclude = ('favorites',)
    list_filter = ('is_premium',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_videos',)
    raw_id_fields = ('videos',)

    def total_videos(self, obj):
        return obj.videos.count()
    total_videos.short_description = 'Total Videos in Category'


admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)
