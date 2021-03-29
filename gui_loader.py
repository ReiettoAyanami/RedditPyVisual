import redditinfo as ri
import utils
import pygame as pg
import button as b
import converter as converter


class gui:
    def __init__(self,surface, limit, sub_name):

        self.limit = limit
        self.sub_name = sub_name
        self.utils = utils
        self.surface = surface
        self.starting_x = 10
        self.starting_y = 200
        self.titles_font = pg.font.Font('fonts/titles/Lexend-Medium.ttf',15)#pg.font.SysFont('Verdana',15)
        self.button_fonts = pg.font.Font('fonts/buttons/Spartan-Light.ttf',15)


        self.nextPostButton = b.Button(self.surface,(0,0,0),(86, 78, 145),(self.starting_x + 105,100,100,50),50,self.button_fonts,'Next Post',True,(86, 78, 145),(0,0,0))
        self.prevPostButton = b.Button(self.surface,(0,0,0),(86, 78, 145),(self.starting_x,100,100,50),50,self.button_fonts,'Prev Post',True,(86, 78, 145),(0,0,0))    
        self.downloadButton = b.Button(self.surface,(0,0,0),(86, 78, 145),(self.starting_x,625,100,50),50,self.button_fonts,'Download',True,(86, 78, 145),(0,0,0))

        self.selected_post = 0
        self.h_fake = 350
        self.subreddit = ri.from_subreddit(self.sub_name,l=self.limit)
        self.subreddit_post = self.subreddit.get_posts()
        self.subreddit_post_urls = self.subreddit.get_url_list()


        self.author_name = self.subreddit_post[self.selected_post].author.name
        self.upvotes = self.subreddit_post[self.selected_post].score
        self.comment_num = self.subreddit_post[self.selected_post].num_comments
        self.title = self.subreddit_post[self.selected_post].title

        self.loader = converter.Loader()
        self.img_list = self.loader.convert_list(self.subreddit_post_urls)
        

        self.image_list = [-1] * self.limit
        
        self.image_list[0] = pg.image.load(self.img_list[0])
        self.w0, self.h0 = self.image_list[0].get_rect().size
        self.image_list[0] = pg.transform.scale(self.image_list[0],(int(self.h_fake/self.h0*self.w0), self.h_fake))
        
        self.image_list[1] = pg.image.load(self.img_list[1])
        self.w1, self.h1 = self.image_list[1].get_rect().size
        self.image_list[1] = pg.transform.scale(self.image_list[1],(int(self.h_fake/self.h1*self.w1), self.h_fake))
        

    def gui_event_handler(self,event):
        if self.nextPostButton.gets_clicked(event):
            
            self.selected_post += 1   
            if self.selected_post >= self.limit:
                self.selected_post = self.limit-1

            try:
                if self.image_list[self.selected_post+1] == -1:
                    try:
                        if self.selected_post < self.limit-1:
                            
                            self.image_list[self.selected_post+1] = pg.image.load(self.img_list[self.selected_post+1])
                            w, h = self.image_list[self.selected_post+1].get_rect().size
                            self.image_list[self.selected_post+1] = pg.transform.scale(self.image_list[self.selected_post+1],(int(self.h_fake/h*w), self.h_fake))

                    except pg.error:
                        pass
            except IndexError:
                pass
              

        if self.prevPostButton.gets_clicked(event):
            self.selected_post -= 1   
            
            if self.selected_post < 0:
                self.selected_post = 0
            
            
            if self.image_list[self.selected_post-1] == -1:
                try:
                    if self.selected_post >= 0:
                        
                        self.image_list[self.selected_post-1] = pg.image.load(self.img_list[self.selected_post-1])
                        w, h = self.image_list[self.selected_post-1].get_rect().size
                        self.image_list[self.selected_post-1] = pg.transform.scale(self.image_list[self.selected_post-1],(int(self.h_fake/h*w), self.h_fake))

                except pg.error:
                    pass
        
        if self.downloadButton.gets_clicked(event):
            self.utils.download(self.subreddit_post_urls[self.selected_post])
            
    


    def main_page_image_displayer(self):
    
        if self.image_list[self.selected_post] == -1:
            noph = self.titles_font.render('No more photos left', True, (0,0,0))
            self.surface.blit(noph,(100,300))
        else:
            try:
                
                 
                self.surface.blit(self.image_list[self.selected_post],(self.starting_x,self.starting_y))   
            except UnboundLocalError:
                noph = self.titles_font.render('No more photos left', True, (0,0,0))
                self.surface.blit(noph,(self.starting_x + 100,300))
    

        
            
    def main_page(self):
        
        pg.draw.rect(self.surface, (192, 184, 255), (self.starting_x-10,self.starting_y - 115,1000,self.h_fake + 245),border_radius = 20)

        self.nextPostButton.show()
        self.prevPostButton.show()
        self.downloadButton.show()
        
        nsfw = ''
        oc = ''
        spoiler = ''

        try:
            self.author_name = self.subreddit_post[self.selected_post].author.name
            self.upvotes = self.subreddit_post[self.selected_post].score
            self.comment_num = self.subreddit_post[self.selected_post].num_comments
            self.title = self.subreddit_post[self.selected_post].title

            if self.subreddit_post[self.selected_post].over_18:
                nsfw = 'NSFW'

            if self.subreddit_post[self.selected_post].is_original_content:
                oc = 'OC'
            if self.subreddit_post[self.selected_post].spoiler:
                spoiler = 'SPOILER'

        except IndexError:
            self.selected_post -= 1

        
        
        nsfw_surf = self.titles_font.render(nsfw,True,(255, 65, 43))
        oc_surf = self.titles_font.render(oc, True, (0, 79, 143))
        spoiler_surf = self.titles_font.render(spoiler, True, (59, 59, 59))
        title_surf = self.titles_font.render(self.title, True, (0,0,0))
        author_surf = self.titles_font.render('Author: '+self.author_name,True,(0,0,0))
        upvotes_surf = self.titles_font.render('This post got: '+ str(self.upvotes)+' upvotes!', True, (0,0,0))
        num_comments_surf = self.titles_font.render(str(self.comment_num)+' people commented this post!', True, (0,0,0))

        nsfw_w = self.titles_font.size(nsfw)[0]
        oc_w = self.titles_font.size(oc)[0]
        post_tag_y = self.starting_y + self.h_fake + 50

        #print(self.selected_post)

        self.surface.blit(author_surf,(self.starting_x,self.starting_y - 50))
        self.surface.blit(title_surf, (self.starting_x, self.starting_y - 25))
        self.surface.blit(upvotes_surf,(self.starting_x,self.starting_y + self.h_fake + 0))  
        self.surface.blit(num_comments_surf,(self.starting_x,self.starting_y + self.h_fake + 25))
        self.surface.blit(nsfw_surf,(self.starting_x,post_tag_y))  
        self.surface.blit(oc_surf,(self.starting_x + (nsfw_w + 10),post_tag_y))
        self.surface.blit(spoiler_surf,(self.starting_x + (nsfw_w + 10) + (oc_w + 10),post_tag_y))
        