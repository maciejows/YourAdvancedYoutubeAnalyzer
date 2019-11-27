import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { ConnectionTestComponent } from './connection-test/connection-test.component';

@NgModule({
  declarations: [
    AppComponent,
    ConnectionTestComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
