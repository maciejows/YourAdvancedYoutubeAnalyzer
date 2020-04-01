import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {

  aboutText: string;

  constructor() { }

  ngOnInit() {
    this.aboutText = "This is project for our Databases lectures at Politechnika Poznańska." 
  }

}
