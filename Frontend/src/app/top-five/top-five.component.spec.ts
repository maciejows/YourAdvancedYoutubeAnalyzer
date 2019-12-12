import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopFiveComponent } from './top-five.component';

describe('TopFiveComponent', () => {
  let component: TopFiveComponent;
  let fixture: ComponentFixture<TopFiveComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopFiveComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopFiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
