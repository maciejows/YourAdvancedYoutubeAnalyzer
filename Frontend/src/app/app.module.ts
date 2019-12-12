import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { TopNavBarComponent } from './top-nav-bar/top-nav-bar.component';
import { BottomNavBarComponent } from './bottom-nav-bar/bottom-nav-bar.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { DataDisplayComponent } from './data-display/data-display.component';
import { AboutComponent } from './about/about.component';
import { TopOneComponent } from './top-one/top-one.component';
import { TopFiveComponent } from './top-five/top-five.component';
import { VideoDisplayComponent } from './video-display/video-display.component';

@NgModule({
  declarations: [
    AppComponent,
    TopNavBarComponent,
    BottomNavBarComponent,
    SearchBarComponent,
    DataDisplayComponent,
    AboutComponent,
    TopOneComponent,
    TopFiveComponent,
    VideoDisplayComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
